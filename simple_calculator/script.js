
document.addEventListener('DOMContentLoaded', function() {
    const displayDiv = document.querySelector('#display');
    let currentValue = '';
    let previousValue = '';
    let operation = null;

    const updateDisplay = (value) => {
        displayDiv.innerText = value;
    };

    const calculate = () => {
        const prev = parseFloat(previousValue);
        const current = parseFloat(currentValue);
        if (isNaN(prev) || isNaN(current)) return;
        switch (operation) {
            case '+':
                currentValue = prev + current;
                break;
            case '-':
                currentValue = prev - current;
                break;
            case '*':
                currentValue = prev * current;
                break;
            case '/':
                if (current === 0) {
                    alert("Cannot divide by zero");
                    currentValue = '';
                    operation = null;
                    return;
                }
                currentValue = prev / current;
                break;
            default:
                return;
        }
        operation = null;
        previousValue = '';
    };

    document.querySelector('.buttons').addEventListener('click', e => {
        if (e.target.matches('button')) {
            const key = e.target.innerText;
            if (!isNaN(key)) {
                if (currentValue.includes('.') && key === '.') return;
                currentValue += key;
                updateDisplay(currentValue);
            } else if (key === 'C') {
                currentValue = '';
                previousValue = '';
                operation = null;
                updateDisplay(0);
            } else if (key === '=') {
                calculate();
                updateDisplay(currentValue);
                currentValue = '';
            } else {
                if (currentValue === '') return;
                if (previousValue !== '') {
                    calculate();
                }
                operation = key;
                previousValue = currentValue;
                currentValue = '';
            }
        }
    });
});