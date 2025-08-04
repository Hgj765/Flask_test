def benford_calculus(x):

    return law_tabel(the_law(x))

def the_law(num):
    numbers = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
    number = int(num)

    while number > 9:
        numbers[str(number)[0]] += int(str(number)[1:]) + 1
        number -= int(str(number)[1:]) + 1

    for i in range(number):
        numbers[str(number)] += 1
        number -= 1
    return numbers

def law_tabel(numbers):
    html="""<table id="data-table">
        <caption>Numbers</caption>
        <thead>
            <tr>
                <th scope="col">1</th>
                <th scope="col">2</th>
                <th scope="col">3</th>
                <th scope="col">4</th>
                <th scope="col">5</th>
                <th scope="col">6</th>
                <th scope="col">7</th>
                <th scope="col">8</th>
                <th scope="col">9</th>
                
            </tr>
        </thead>
        <tbody>
        <tr>
        """
    for i in numbers:
        html += f"<td>{numbers[i]}</td>"
    html+="""</tr>
        </tbody>"""
    return html
