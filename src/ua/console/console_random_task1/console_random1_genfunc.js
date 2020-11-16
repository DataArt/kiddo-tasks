const lowercaseLetters = generateCharArray('A', 'Y');

const randomAmountOfVariables = getRandomInt(1, 5);

const variables = [];

for (let i = 0; i < randomAmountOfVariables; i++) {
    const randomLetterIndex = Math.floor(Math.random() * lowercaseLetters.length);
    const randomVarName = lowercaseLetters[randomLetterIndex];
    lowercaseLetters.splice(randomLetterIndex, 1);
    const randomVariable = {
        name: randomVarName,
        value: getRandomInt(1, 100),
        readOnly: true
    };
    variables.push(randomVariable);
}

const randomizedFormula = variables.map(variable => variable.name).join(' + ');

variables.push({ name: 'Z', value: null });

for (let i = 0; i < variables.length; i++) {
    this.consoleSceneWriterService.addConsoleVariable(variables[i]);
}

const winCondition = {
    consoleVariables: [{
        name: 'Z',
        value: '',
        formula: randomizedFormula
    }]
}

this.addWinCondition(winCondition);



function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function generateCharArray(from, to) {
    from = from.charCodeAt(0);
    to = to.charCodeAt(0);
    const result = [];
    for (let i = from; i < to; i++) {
        result.push(String.fromCharCode(i));
    }
    return result;
}