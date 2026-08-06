import XCTest
@testable import AlgorithmPractiseLibrary

final class LongestSubstringWithoutRepeatingCharactersTests: XCTestCase {

    private let solution = LongestSubstringWithoutRepeatingCharacters()

    func testExample_abcabcbb() {
        XCTAssertEqual(solution.lengthOfLongestSubstring("abcabcbb"), 3)
    }

    func testAllRepeating_bbbbb() {
        XCTAssertEqual(solution.lengthOfLongestSubstring("bbbbb"), 1)
    }

    func testExample_pwwkew() {
        XCTAssertEqual(solution.lengthOfLongestSubstring("pwwkew"), 3)
    }

    func testEmptyString() {
        XCTAssertEqual(solution.lengthOfLongestSubstring(""), 0)
    }

    func testSingleCharacter() {
        XCTAssertEqual(solution.lengthOfLongestSubstring("a"), 1)
    }

    func testAllUnique() {
        XCTAssertEqual(solution.lengthOfLongestSubstring("abcdef"), 6)
    }

    func testRepeatingAtEnd() {
        XCTAssertEqual(solution.lengthOfLongestSubstring("abcdea"), 5)
    }

    func testTwoCharAlternating() {
        XCTAssertEqual(solution.lengthOfLongestSubstring("ababab"), 2)
    }

    func testWithSpaces() {
        // spaces repeat, longest window is "a b" or "b c" etc. = 3
        XCTAssertEqual(solution.lengthOfLongestSubstring("a b c d"), 3)
    }

    func testWithNumbers() {
        XCTAssertEqual(solution.lengthOfLongestSubstring("123412345"), 5)
    }
}
