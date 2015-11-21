// ImgCmp.cpp : Defines the exported functions for the DLL application.
//

#include "stdafx.h"
#include "ImgCmp.h"

#include <opencv2\opencv.hpp>


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

	cv::Mat diff, bin, cc_lbl, cc_stats, cc_centroids, k;

	cv::Mat ref_im = cv::imread(ref_image, cv::IMREAD_GRAYSCALE);
	cv::Mat test_im = cv::imread(test_image, cv::IMREAD_GRAYSCALE);

	cv::absdiff(ref_im, test_im, diff);

	double tresh_val = cv::threshold(diff, bin, 0.0, 255.0, cv::THRESH_OTSU + cv::THRESH_BINARY);

	k = cv::getStructuringElement(cv::MORPH_ELLIPSE, cv::Size(5, 5));

	cv::morphologyEx(bin, bin, cv::MORPH_CLOSE, k);

	int num_cc = cv::connectedComponentsWithStats(bin, cc_lbl, cc_stats, cc_centroids);

	for (int l = 1; l < (int)num_cc; ++l) {
		ImgDiff d;

		int *row = (int *)&cc_stats.at<int>(l, 0);

		d.left = row[cv::CC_STAT_LEFT];
		d.top = row[cv::CC_STAT_TOP];
		d.width = row[cv::CC_STAT_WIDTH];
		d.height = row[cv::CC_STAT_HEIGHT];

		auto sum = cv::sum(
			diff(cv::Range(d.top, d.top + d.height), cv::Range(d.left, d.left + d.width))
			);

		d.sad = sum(0) / (d.width * d.height);

		result.push_back(d);

		row[cv::CC_STAT_AREA];
	}


	

	return result;
}

