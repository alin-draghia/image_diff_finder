#pragma once

#ifndef __IMG_CMP_H__
#define __IMG_CMP_H__

#include <string>
#include <vector>



struct ImgDiff {
	int left;
	int top;
	int width;
	int height;

	// Sum of absolute difference
	float sad;

	ImgDiff();
	ImgDiff(int left, int top, int width, int height, float sad);
};


class ImgCmp {
public:
	ImgCmp();
	std::vector<ImgDiff> CompareImages(const std::string& ref_image, const std::string& test_image) const;
};


#endif