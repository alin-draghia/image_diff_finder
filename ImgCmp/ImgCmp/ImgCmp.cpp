// ImgCmp.cpp : Defines the exported functions for the DLL application.
//

#include "stdafx.h"
#include "ImgCmp.h"



ImgDiff::ImgDiff()
{
	left = 0;
	top = 0;
	width = 0;
	height = 0;
	sad = 0.0f;
}

ImgDiff::ImgDiff(int left, int top, int width, int height, float sad)
{
	this->left = left;
	this->top = top;
	this->width = width;
	this->height = height;
	this->sad = sad;
}

ImgCmp::ImgCmp()
{
}

std::vector<ImgDiff> ImgCmp::CompareImages(const std::string & ref_image, const std::string & test_image) const
{
	std::vector<ImgDiff> result;

	ImgDiff d = { 10, 20, 64, 32, 13.6f };
	ImgDiff d2 = { 100, 200, 640, 320, 130.6f };
	result.push_back(d);
	result.push_back(d2);

	return result;
}

