# 讀取函式
def read_file(filename):
	lines = []
	with open(filename, "r", encoding = "utf-8-sig") as f:
		for line in f:
			lines.append(line.strip())
	return lines

# 格式轉換
def convert(lines):
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(" ")
		time = s[0]
		name = s[1]
		if "Allen" in s:
			if s[2] == "貼圖":
				allen_sticker_count += 1
			elif s[2] == "圖片":
				allen_image_count += 1
			else :
				for msg in s[2:]:
					allen_word_count += len(msg)
		elif "Viki" in s:
			if s[2] == "貼圖":
				viki_sticker_count += 1
			elif s[2] == "圖片":
				viki_image_count += 1
			else:
				for msg in s[2:]:
					viki_word_count += len(msg)
	print(f"Allen傳了{allen_word_count}個字")
	print(f"Allen傳了{allen_sticker_count}個貼圖")
	print(f"Allen傳了{allen_image_count}張圖片")
	print(f"Viki傳了{viki_word_count}個字")
	print(f"Viki傳了{viki_sticker_count}個貼圖")
	print(f"Viki傳了{viki_image_count}張圖片")


# 寫入函式
def write_file(filename, lines):
	with open(filename, "w") as f:
		for line in lines:
			f.write(line)

def main():
	lines = read_file("LINE-Viki.txt")
	lines = convert(lines)
	# write_file("output2.txt", lines)

main()