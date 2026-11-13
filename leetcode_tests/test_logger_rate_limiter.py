import pytest
from leetcode.logger_rate_limiter import Logger


class TestLoggerRateLimiter:
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.logger = Logger()

    def test_leetcode_example(self):
        """Test the official example."""
        calls = [(1, "foo"), (2, "bar"), (3, "foo"), (8, "bar"), (10, "foo"), (11, "foo")]
        expected = [True, True, False, False, False, True]
        assert [self.logger.shouldPrintMessage(t, m) for t, m in calls] == expected

    def test_first_message_always_printed(self):
        assert self.logger.shouldPrintMessage(0, "a") is True

    def test_timestamp_zero_blocks_until_ten(self):
        """A message at t=0 is blocked until t=10."""
        assert self.logger.shouldPrintMessage(0, "a") is True
        assert self.logger.shouldPrintMessage(9, "a") is False
        assert self.logger.shouldPrintMessage(10, "a") is True

    def test_boundary_exactly_ten_seconds(self):
        assert self.logger.shouldPrintMessage(5, "a") is True
        assert self.logger.shouldPrintMessage(14, "a") is False
        assert self.logger.shouldPrintMessage(15, "a") is True

    def test_same_timestamp_duplicate(self):
        """Identical messages at the same timestamp: only the first is printed."""
        assert self.logger.shouldPrintMessage(1, "a") is True
        assert self.logger.shouldPrintMessage(1, "a") is False

    def test_same_timestamp_different_messages(self):
        assert self.logger.shouldPrintMessage(1, "a") is True
        assert self.logger.shouldPrintMessage(1, "b") is True

    def test_messages_are_independent(self):
        assert self.logger.shouldPrintMessage(1, "a") is True
        assert self.logger.shouldPrintMessage(2, "b") is True
        assert self.logger.shouldPrintMessage(5, "a") is False
        assert self.logger.shouldPrintMessage(12, "b") is True

    def test_blocked_call_does_not_extend_window(self):
        """A rejected message must not reset the 10-second window."""
        assert self.logger.shouldPrintMessage(1, "a") is True
        assert self.logger.shouldPrintMessage(8, "a") is False
        assert self.logger.shouldPrintMessage(11, "a") is True

    def test_printed_message_resets_window(self):
        assert self.logger.shouldPrintMessage(1, "a") is True
        assert self.logger.shouldPrintMessage(11, "a") is True
        assert self.logger.shouldPrintMessage(20, "a") is False
        assert self.logger.shouldPrintMessage(21, "a") is True

    def test_large_timestamp(self):
        big = 10**9
        assert self.logger.shouldPrintMessage(big - 10, "a") is True
        assert self.logger.shouldPrintMessage(big - 1, "a") is False
        assert self.logger.shouldPrintMessage(big, "a") is True

    def test_many_unique_messages(self):
        for i in range(1000):
            assert self.logger.shouldPrintMessage(i, f"msg{i}") is True

    def test_instances_are_independent(self):
        other = Logger()
        assert self.logger.shouldPrintMessage(1, "a") is True
        assert other.shouldPrintMessage(2, "a") is True

    @pytest.mark.parametrize("calls,expected", [
        ([(0, "a"), (10, "a")], [True, True]),
        ([(0, "a"), (9, "a")], [True, False]),
        ([(1, "a"), (2, "b"), (3, "a"), (12, "b")], [True, True, False, True]),
        ([(100, "x"), (100, "x"), (110, "x"), (119, "x"), (120, "x")],
         [True, False, True, False, True]),
    ])
    def test_parametrized_cases(self, calls, expected):
        assert [self.logger.shouldPrintMessage(t, m) for t, m in calls] == expected


if __name__ == "__main__":
    pytest.main([__file__])
