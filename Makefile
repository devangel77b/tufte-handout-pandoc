BUILDDIR=build
FILENAME=foo

test:
	mkdir -p $(BUILDDIR)
	pandoc $(FILENAME).md \
	--from=markdown+tex_math_dollars \
	--to=latex \

tex:
	mkdir -p $(BUILDDIR)
	pandoc $(FILENAME).md \
	--from=markdown+tex_math_dollars \
	--to=latex \
	--output=$(BUILDDIR)/$(FILENAME).tex \
	--standalone
