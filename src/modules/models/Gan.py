import numpy as np
import tensorflow.python.keras as keras

from src.modules.data.GanTrainingDatum import GanTrainingDatum
from src.modules.models.Discriminator import Discriminator
from src.modules.models.Generator import Generator


class Gan:
	def __init__(
		self,
		*,
		discriminator: Discriminator,
		generator: Generator,
	) -> None:
		super().__init__()
		self._model = keras.models.Sequential()
		self._generator = generator
		self._discriminator = discriminator
		self._model.add(self._generator.model)
		self._model.add(self._discriminator.model)
		self._model.compile(
			loss=["binary_crossentropy", "binary_crossentropy"],
			optimizer="adam",
			metrics=["accuracy"],
		)

	@property
	def model(self) -> keras.Model:
		return self._model
	
	@property
	def discriminator(self) -> Discriminator:
		return self._discriminator

	@property
	def generator(self) -> Generator:
		return self._generator

	def train(
		self,
		data: list[GanTrainingDatum],
	) -> None:
		x: np.ndarray = np.array(
			[np.concatenate((datum.discriminations, datum.noise), axis=None) for datum in data]
		)
		y: np.ndarray = np.array(
			[datum.discriminations for datum in data]
		)

		self._model.train_on_batch(x, y)
