import logging
import os

log = logging.getLogger(__name__)


class FileUtil:
    TMP_PATH = "/tmp/"

    @classmethod
    def store_image_and_get_temp_path(cls, document, document_name):
        file_path = f'{FileUtil.get_temp_directory()}/{document_name}'

        with open(file_path, "w") as image:
            image.write(document)

        return file_path

    @classmethod
    def get_temp_directory(cls):
        return

    @classmethod
    def create_directory(cls, directory_path):
        try:
            os.mkdir(directory_path)
            log.debug('Directory created at:{}'.format(directory_path))
        except OSError:
            log.error('Directory already exists at: {}'.format(directory_path))

    @classmethod
    def remove_file(cls, file_path):
        try:
            os.remove(file_path)
            log.debug("Removed file at: {}".format(file_path))
        except OSError:
            log.warn("File not present at: {}".format(file_path))


FileUtil.create_directory(FileUtil.TMP_PATH)
