from typing import Optional
from src.modules.abstract.LabelExtractor import LabelExtractor
import re


class RegexLabelExtractor(LabelExtractor):
	def __init__(self, regexString: str) -> None:
		self._regex: re.Pattern = re.compile(regexString)

	@property
	def regex(self) -> re.Pattern:
		return self._regex

	def extract(self, filepath: str) -> set[str]:
		match: Optional[re.Match] = self._regex.match(filepath)
		if match is None:
			raise RuntimeError(f"{filepath} does not match {self._regex}")
		return {match.group(1)}
