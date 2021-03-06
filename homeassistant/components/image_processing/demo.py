"""
Support for the demo image processing.

For more details about this component, please refer to the documentation at
https://home-assistant.io/components/demo/
"""
from homeassistant.components.image_processing import ATTR_CONFIDENCE
from homeassistant.components.image_processing.openalpr_local import (
    ImageProcessingAlprEntity)
from homeassistant.components.image_processing.microsoft_face_identify import (
    ImageProcessingFaceEntity, ATTR_NAME, ATTR_AGE, ATTR_GENDER)


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the demo image_processing platform."""
    add_devices([
        DemoImageProcessingAlpr('camera.demo_camera', "Demo Alpr"),
        DemoImageProcessingFace(
            'camera.demo_camera', "Demo Face")
    ])


class DemoImageProcessingAlpr(ImageProcessingAlprEntity):
    """Demo alpr image processing entity."""

    def __init__(self, camera_entity, name):
        """Initialize demo alpr."""
        super().__init__()

        self._name = name
        self._camera = camera_entity

    @property
    def camera_entity(self):
        """Return camera entity id from process pictures."""
        return self._camera

    @property
    def confidence(self):
        """Return minimum confidence for send events."""
        return 80

    @property
    def name(self):
        """Return the name of the entity."""
        return self._name

    def process_image(self, image):
        """Process image."""
        demo_data = {
            'AC3829': 98.3,
            'BE392034': 95.5,
            'CD02394': 93.4,
            'DF923043': 90.8
        }

        self.process_plates(demo_data, 1)


class DemoImageProcessingFace(ImageProcessingFaceEntity):
    """Demo face identify image processing entity."""

    def __init__(self, camera_entity, name):
        """Initialize demo alpr."""
        super().__init__()

        self._name = name
        self._camera = camera_entity

    @property
    def camera_entity(self):
        """Return camera entity id from process pictures."""
        return self._camera

    @property
    def confidence(self):
        """Return minimum confidence for send events."""
        return 80

    @property
    def name(self):
        """Return the name of the entity."""
        return self._name

    def process_image(self, image):
        """Process image."""
        demo_data = [
            {
                ATTR_CONFIDENCE: 98.34,
                ATTR_NAME: 'Hans',
                ATTR_AGE: 16.0,
                ATTR_GENDER: 'male',
            },
            {
                ATTR_NAME: 'Helena',
                ATTR_AGE: 28.0,
                ATTR_GENDER: 'female',
            },
            {
                ATTR_CONFIDENCE: 62.53,
                ATTR_NAME: 'Luna',
            },
        ]

        self.process_faces(demo_data, 4)
