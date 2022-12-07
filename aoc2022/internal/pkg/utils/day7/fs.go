package day7

import (
	"fmt"
	"strconv"
	"strings"
)

type dir struct {
	name     string
	parent   *dir
	contents []*dir
	size     int
}

func (d *dir) getParent() *dir {
	return d.parent
}

func (d *dir) getSize() int {
	size := d.size
	for _, c := range d.contents {
		size += c.getSize()
	}
	return size
}

func (d *dir) getSumDirSize(thresshold int) int {
	size := 0
	dirSize := d.getSize()
	if dirSize <= thresshold {
		size += dirSize
	}

	for _, child := range d.contents {
		size += child.getSumDirSize(thresshold)
	}

	return size
}

func (d *dir) getSmallestDirSize(thresshold int) int {
	smallest := d.getSize()

	for _, child := range d.contents {
		dirSize := child.getSmallestDirSize(thresshold)
		if dirSize > thresshold && dirSize < smallest {
			smallest = dirSize
		}
	}

	return smallest
}

func (d *dir) getName() string {
	return d.name
}

func (d *dir) print(indent int) {
	fmt.Printf("%s- %s (dir, size=%d)\n", strings.Repeat(" ", indent), d.name, d.size)
	for _, c := range d.contents {
		c.print(indent + 2)
	}
}

func (d *dir) add(newDir *dir) {
	d.contents = append(d.contents, newDir)
}

func newDir(name string, parent *dir) *dir {
	return &dir{name: name, parent: parent, size: 0}
}

type Fs struct {
	root       *dir
	currentDir *dir
}

func (f *Fs) AddDir(dir string) {
	f.currentDir.add(newDir(dir, f.currentDir))
}

func (f *Fs) AddFile(fileData string) {
	fileParts := strings.Split(fileData, " ")
	size, err := strconv.Atoi(fileParts[0])
	if err != nil {
		panic(err)
	}

	f.currentDir.size += size
}

func (f *Fs) Cd(dirName string) {
	if f.currentDir == nil && dirName == f.root.name {
		f.currentDir = f.root
		return
	}

	if dirName == ".." {
		f.currentDir = f.currentDir.parent
	}

	for _, c := range f.currentDir.contents {
		if c.getName() == dirName {
			f.currentDir = c
			break
		}
	}
}

func (f *Fs) Ls() {
	f.root.print(0)
}

func (f *Fs) GetSumDirSize(thresshold int) int {
	total := f.root.getSumDirSize(thresshold)

	return total
}

func (f *Fs) GetSmallestDirSize(thresshold int) int {
	total := f.root.getSmallestDirSize(thresshold)

	return total
}

func (f *Fs) GetSize() int {
	return f.root.getSize()
}

func NewFs(root string) *Fs {
	dir := newDir("/", nil)
	return &Fs{root: dir}
}
