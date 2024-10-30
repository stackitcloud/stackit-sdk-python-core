import time
from http import HTTPStatus

import signal
import contextlib
from typing import Any, Callable, Tuple, Union


class Wait:

    RetryHttpErrorStatusCodes = [HTTPStatus.BAD_GATEWAY, HTTPStatus.GATEWAY_TIMEOUT]

    def __init__(
        self,
        check_function: Callable[[None], Tuple[bool, Union[Exception, None], Union[int, None], Any]],
        sleep_before_wait: int = 0,
        throttle: int = 5,
        timeout: int = 30,
        temp_error_retry_limit: int = 5,
    ) -> None:
        if throttle == 0:
            raise ValueError("throttle can't be 0")
        self._check_function = check_function
        self._sleep_before_wait = sleep_before_wait
        self._throttle = throttle
        self._timeout = timeout * 60
        self._temp_error_retry_limit = temp_error_retry_limit
        self.retry_http_error_status_codes = [HTTPStatus.BAD_GATEWAY, HTTPStatus.GATEWAY_TIMEOUT]

    @staticmethod
    def _timeout_handler(signum, frame):
        raise TimeoutError("Wait has timed out")

    def wait(self) -> Any:
        time.sleep(self._sleep_before_wait)

        retry_temp_error_counter = 0

        signal.signal(signal.SIGALRM, Wait._timeout_handler)
        signal.alarm(self._timeout)

        while True:

            done, error, code, result = self._check_function()
            if error:
                retry_temp_error_counter = self._handle_error(retry_temp_error_counter, error, code)

            if done:
                return result
            time.sleep(self._throttle)

    def _handle_error(self, retry_temp_error_counter: int, error, code: int):

        if code in self.retry_http_error_status_codes:
            retry_temp_error_counter += 1
            if retry_temp_error_counter == self._temp_error_retry_limit:
                raise error
            return retry_temp_error_counter
        else:
            raise error
