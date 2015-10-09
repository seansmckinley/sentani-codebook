.PHONY: all_ipynb all_markdown
all_markdown: codebook-section-1.md  codebook-section-2.md codebook-section-3.md codebook-section-4.md codebook-section-5.md codebook-section-6.md codebook-section-7.md
all_ipynb: codebook-section-1.ipynb  codebook-section-2.ipynb codebook-section-3.ipynb codebook-section-4.ipynb codebook-section-5.ipynb codebook-section-6.ipynb codebook-section-7.ipynb


codebook-section-1.md: codebook-section-1.ipynb
	notedown codebook-section-1.ipynb --to markdown --strip > codebook-section-1.md
codebook-section-2.md: codebook-section-2.ipynb
	notedown codebook-section-2.ipynb --to markdown --strip > codebook-section-2.md
codebook-section-3.md: codebook-section-3.ipynb
	notedown codebook-section-3.ipynb --to markdown --strip > codebook-section-3.md
codebook-section-4.md: codebook-section-4.ipynb
	notedown codebook-section-4.ipynb --to markdown --strip > codebook-section-4.md
codebook-section-5.md: codebook-section-5.ipynb
	notedown codebook-section-5.ipynb --to markdown --strip > codebook-section-5.md
codebook-section-6.md: codebook-section-6.ipynb
	notedown codebook-section-6.ipynb --to markdown --strip > codebook-section-6.md
codebook-section-7.md: codebook-section-7.ipynb
	notedown codebook-section-7.ipynb --to markdown --strip > codebook-section-7.md

codebook-section-1.ipynb:
	notedown codebook-section-1.md --run > codebook-section-1.ipynb
codebook-section-2.ipynb:
	notedown codebook-section-2.md --run > codebook-section-2.ipynb
codebook-section-3.ipynb:
	notedown codebook-section-3.md --run > codebook-section-3.ipynb
codebook-section-4.ipynb:
	notedown codebook-section-4.md --run > codebook-section-4.ipynb
codebook-section-5.ipynb:
	notedown codebook-section-5.md --run > codebook-section-5.ipynb
codebook-section-6.ipynb:
	notedown codebook-section-6.md --run > codebook-section-6.ipynb
codebook-section-7.ipynb:
	notedown codebook-section-7.md --run > codebook-section-7.ipynb





