import * as fs from 'fs';

type NumberIndex = {
    index: number;
    value: string
}

const getNumbersIndicesFromString = (input: string): NumberIndex[] => {
    return [...input.matchAll(/\d/gi)]
        .map(a => ({ index: a.index, value: a[0] }))
        .sort((a, b) => a.index - b.index)
}

const getTargetNumbersFromNumberIndices = (numberIndices: NumberIndex[]): number => {
    const firstDigit = numberIndices[0].value
    const lastDigit = numberIndices[numberIndices.length-1].value
    return parseInt(firstDigit + lastDigit)
}

export const extractTwoDigitNumber = (input: string) => {
    const array = getNumbersIndicesFromString(input)
    return(getTargetNumbersFromNumberIndices(array))
}

export const extractRealNumbersFromString = (input: string) => {
    const numericIndices = getNumbersIndicesFromString(input)
    const numberWordsIncluded = numericIndices
        .concat([...input.matchAll(/one/gi)].map(a => ({ index: a.index, value: '1' })))
        .concat([...input.matchAll(/two/gi)].map(a => ({ index: a.index, value: '2' })))
        .concat([...input.matchAll(/three/gi)].map(a => ({ index: a.index, value: '3' })))
        .concat([...input.matchAll(/four/gi)].map(a => ({ index: a.index, value: '4' })))
        .concat([...input.matchAll(/five/gi)].map(a => ({ index: a.index, value: '5' })))
        .concat([...input.matchAll(/six/gi)].map(a => ({ index: a.index, value: '6' })))
        .concat([...input.matchAll(/seven/gi)].map(a => ({ index: a.index, value: '7' })))
        .concat([...input.matchAll(/eight/gi)].map(a => ({ index: a.index, value: '8' })))
        .concat([...input.matchAll(/nine/gi)].map(a => ({ index: a.index, value: '9' })))
        .sort((a, b) => a.index - b.index)

    return(getTargetNumbersFromNumberIndices(numberWordsIncluded))
}

const challenge1 = (lines: string[]) => {
    const result = lines
        .map((line: string) => (extractTwoDigitNumber(line)))
        .reduce((current, total) => current + total, 0)
    console.log("challenge 1: " + result)
}

const challenge2 = (lines: string[]) => {
    const result = lines
        .map((line: string) => (extractRealNumbersFromString(line)))
        .reduce((current, total) => current + total, 0)
    console.log("challenge 2: " + result)
}

const day1 = () => {
    const data = fs.readFileSync('./input.txt', 'utf-8');
    const lines = data.split('\r\n')

    challenge1(lines);
    challenge2(lines);
}

day1();