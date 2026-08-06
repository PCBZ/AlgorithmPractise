import XCTest
@testable import AlgorithmPractiseLibrary

final class PermutationsIITests: XCTestCase {

    private let solution = Solution()

    // Normalizes result for order-independent comparison
    private func sorted(_ permutations: [[Int]]) -> [[Int]] {
        permutations.map { $0 }.sorted(by: { $0.lexicographicallyPrecedes($1) })
    }

    func testWithDuplicates() {
        let result = solution.permuteUnique([1, 1, 2])
        let expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        XCTAssertEqual(sorted(result), sorted(expected))
    }

    func testAllDuplicates() {
        let result = solution.permuteUnique([1, 1, 1])
        XCTAssertEqual(result, [[1, 1, 1]])
    }

    func testNoDuplicates() {
        let result = solution.permuteUnique([1, 2, 3])
        let expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        XCTAssertEqual(sorted(result), sorted(expected))
        XCTAssertEqual(result.count, 6)
    }

    func testSingleElement() {
        XCTAssertEqual(solution.permuteUnique([1]), [[1]])
    }

    func testTwoIdenticalElements() {
        XCTAssertEqual(solution.permuteUnique([2, 2]), [[2, 2]])
    }

    func testTwoDifferentElements() {
        let result = solution.permuteUnique([1, 2])
        let expected = [[1, 2], [2, 1]]
        XCTAssertEqual(sorted(result), sorted(expected))
    }

    func testNoDuplicatePermutations() {
        // Ensure no result appears more than once
        let result = solution.permuteUnique([1, 1, 2])
        let unique = Set(result.map { $0.description })
        XCTAssertEqual(result.count, unique.count)
    }
}
