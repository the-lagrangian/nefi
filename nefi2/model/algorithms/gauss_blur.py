# -*- coding: utf-8 -*-
"""
This class represents the algorithm Gaussian Blur from the opencv package
"""
__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}

import cv2
from _alg import Algorithm, IntegerSlider, FloatSlider


class AlgBody(Algorithm):
    """Gaussian Blur algorithm implementation"""
    def __init__(self):
        """
        Gaussian Blur object constructor
        Instance vars:
            self.name -- name of the algorithm
            self.parent -- name of the appropriated category
            self.kernelsize -- blurring kernel size that will be used as slider for the UI
            self.sigmaX -- gaussian kernel standard deviation in X direction
        """
        self.name = "Gaussian Blur"
        self.parent = "Preprocessing"
        self.kernelsize = IntegerSlider(self,"kernelsize",1,1,20)
        self.sigmaX = FloatSlider(self,"sigmaX",1,1,100)

    def process(self, image):
        """
        Use the gaussian blur algorithm from the opencv package to the current image
        Args:
            image: image instance

        """
        self.result =  cv2.GaussianBlur(image,(self.kernelsize.value*2+1,self.kernelsize.value*2+1),self.sigmaX)


    def belongs(self):
        """
        Define method membership (category)
        Returns: name of the appropriated category

        """
        return self.parent

    def get_name(self):
        """
        Define algorithm name that will be displayed in UI
        Returns: algorithm name

        """
        return self.name

    def sign(self, image, settings):
        """
        Save the name of the current algorithm and settings used to process
        the image in the image class
        Args:
            image: image instance
            settings: dict of settings used by the algorithm

        Returns:

        """
        pass
        #image.sign(self.name, settings)

if __name__ == '__main__':
    pass

