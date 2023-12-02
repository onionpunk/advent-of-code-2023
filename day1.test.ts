import 'jest';

import { 
    extractTwoDigitNumber, 
    extractRealNumbersFromString
} from './day1'

describe('challenge1: digits extraction', () => {
    describe('digits at the beginning and end of string', () => {
        it('should extract the digits', () => {
            const input: string = "1abc2"
            const expected: number = 12
            const result = extractTwoDigitNumber(input)
            expect(result).toEqual(expected)
        })
    })
    
    describe('string with two digits in the middle', () => {
        it('should extract the two digits', () => {
            const input: string = "pqr3stu8vwx"
            const expected: number = 38
            const result = extractTwoDigitNumber(input)
            expect(result).toEqual(expected)
        })
    })

    describe('string with multiple digits', () => {
        it('should extract the digits based on the first and last digit', () => {
            const input: string = "a1b2c3d4e5f"
            const expected: number = 15
            const result = extractTwoDigitNumber(input)
            expect(result).toEqual(expected)
        })
    })

    
    describe('string with a single digit', () => {
        it('should extract the only digit and make it repeated', () => {
            const input: string = "treb7uchet"
            const expected: number = 77
            const result = extractTwoDigitNumber(input)
            expect(result).toEqual(expected)
        })
    })
})

describe('challenge2: word as digits', () => {
    describe('strings that contain 2 words as digits', () => {
        it('should convert the words into numbers', () => {
            const input: string = "two1nine"
            const expected: number = 29
            const result = extractRealNumbersFromString(input)
            expect(result).toEqual(expected)
        })
    })

    describe('strings that has all words as digits', () => {
        it('should convert the words into numbers', () => {
            const input: string = "eightwothree"
            const expected: number = 83
            const result = extractRealNumbersFromString(input)
            expect(result).toEqual(expected)
        })
    })

    describe('strings that has random characters, words as digits, and an actual number', () => {
        it('should convert the words into numbers', () => {
            const input: string = "abcone2threexyz"
            const expected: number = 13
            const result = extractRealNumbersFromString(input)
            expect(result).toEqual(expected)
        })
    })

    describe('strings that has overlapping number words', () => {
        it('should convert the first overlapping word into number', () => {
            const input: string = "xtwone3four"
            const expected: number = 24
            const result = extractRealNumbersFromString(input)
            expect(result).toEqual(expected)
        })

        it('should convert the first overlapping word into number', () => {
            const input: string = "zoneight234"
            const expected: number = 14
            const result = extractRealNumbersFromString(input)
            expect(result).toEqual(expected)
        })
    })

    describe('strings that begins and ends with digits', () => {
        it('should convert the words into numbers but leave the beginning and end digit the same', () => {
            const input: string = "4nineeightseven2"
            const expected: number = 42
            const result = extractRealNumbersFromString(input)
            expect(result).toEqual(expected)
        })
    })

    describe('strings that contains number word sixteen', () => {
        it('should ignore the teen bit', () => {
            const input: string = "7pqrstsixteen"
            const expected: number = 76
            const result = extractRealNumbersFromString(input)
            expect(result).toEqual(expected)
        })
    })
})


