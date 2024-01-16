import random
import PySimpleGUI as sg


def acey_deucy():
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    cash = 100
    while cash > 0:
        print(f"You have {cash} dollars.")
        wager = int(input("How much would you like to bet? "))
        if wager > cash:
            print("You don't have enough money to make that bet.")
            continue
        cash -= wager
        random.shuffle(deck)
        card1, card2 = deck.pop(), deck.pop()
        print(f"Your cards are {card1} and {card2}.")
        in_between = input("Do you think the next card will be in between? (y/n) ")
        if in_between.lower() == 'y':
            card3 = deck.pop()
            print(f"The next card is {card3}.")
            if card1 < card3 < card2 or card2 < card3 < card1:
                cash += wager * 2
                print(f"You win! You now have {cash} dollars.")
            else:
                print(f"You lose. You now have {cash} dollars.")
        elif in_between.lower() == 'n':
            card3 = deck.pop()
            print(f"The next card is {card3}.")
            if card3 <= card1 or card3 >= card2:
                cash += wager * 2
                print(f"You win! You now have {cash} dollars.")
            else:
                print(f"You lose. You now have {cash} dollars.")
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    print("You're out of money. Game over!")


def acey_deucy_ui():
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    cash = 100
    sg.theme("Green")
    layout = [
        [sg.Text(f"You have {cash} dollars.", key='-CASH-')],
        [sg.Text("How much would you like to bet? "), sg.InputText(key='-WAGER-')],
        [sg.Button("Deal"), sg.Button("Cash Out")]
    ]
    window = sg.Window("Acey Deucy", layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Cash Out":
            if cash < 100:
                sg.popup("The House Always WINS!!")
            break
        if event == "Deal":
            try:
                wager = int(values['-WAGER-'])
            except ValueError:
                sg.popup("Invalid input. Please enter a valid integer.")
                continue
            if wager > cash:
                sg.popup("You don't have enough money to make that bet.")
                continue
            cash -= wager
            window['-CASH-'].update(f"You have {cash} dollars.")
            random.shuffle(deck)
            card1, card2 = random.choice(deck), random.choice(deck)
            in_between_layout = [
                [sg.Text(f"Your cards are {card1} and {card2}.")],
                [sg.Text("Do you think the next card will be in between?")],
                [sg.Button("Yes"), sg.Button("No")]
            ]
            in_between_window = sg.Window("In Between?", in_between_layout)
            in_between_event, _ = in_between_window.read()
            in_between_window.close()
            if in_between_event == "Yes":
                card3 = random.choice(deck)
                sg.popup(f"The next card is {card3}.")
                if card1 < card3 < card2 or card2 < card3 < card1:
                    cash += wager * 2
                    sg.popup(f"You win! You now have {cash} dollars.")
                else:
                    sg.popup(f"You lose. You now have {cash} dollars.")
            elif in_between_event == "No":
                card3 = random.choice(deck)
                sg.popup(f"The next card is {card3}.")
                if card3 <= card1 or card3 >= card2:
                    cash += wager * 2
                    sg.popup(f"You win! You now have {cash} dollars.")
                else:
                    sg.popup(f"You lose. You now have {cash} dollars.")
            else:
                sg.popup("Invalid input. Please enter 'Yes' or 'No'.")
    window.close()
