#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import deque
from PyQt5 import QtWidgets, QtGui, QtCore
from quadtree import QuadTree, QuadTreeNode
from point import Point

class QuadTreeWindow(QtWidgets.QMainWindow):
    background = QtGui.QColor(27, 52, 108)
    normal = QtGui.QColor(1, 171, 233, 32)
    points = QtGui.QColor(1, 171, 233)
    fill = QtGui.QColor(195, 206, 208, 8)
    foundpoints = QtGui.QColor(245, 75, 26)
    searched = QtGui.QColor(245, 75, 26, 64)
    searchring = QtGui.QColor(229, 195, 158)

    def __init__(self):
        self.root = QuadTree()
        self.radius = 0.125
        self.searching = None
        self.found = []

        self.app = QtWidgets.QApplication(sys.argv)
        super().__init__()

        self.app.setStyle("Fusion")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, self.background)
        self.app.setPalette(palette)

        self.setWindowTitle('QuadTree')
        self.resize(600, 600)
        self.show()
        # main event loop
        sys.exit(self.app.exec_())

    def keyPressEvent(self, event):
        from random import randint
        if event.key() == QtCore.Qt.Key_Q:
            self.app.quit()
        elif event.key() == QtCore.Qt.Key_A:
            self.radius *= 9 / 8
        elif event.key() == QtCore.Qt.Key_Z:
            self.radius *= 7 / 8
        elif event.key() == QtCore.Qt.Key_Space:
            width, height = self.geometry().width(), self.geometry().height()
            for _ in range(150):
                self.root.insert(Point(
                    randint(0, width) / width,
                    randint(0, height) / height
                ))
            self.update()
        event.accept()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            geometry = self.geometry()
            width, height = geometry.width(), geometry.height()
            pos = event.pos()
            self.searching = pos
            self.found = self.root.search(
                Point(pos.x() / width, pos.y() / height),
                self.radius
            )
            self.update()
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.searching = None
            self.found = []
            self.root.unmark()
            self.update()
            event.accept()
            return
        elif event.button() == QtCore.Qt.LeftButton:
            geometry = self.geometry()
            width, height = geometry.width(), geometry.height()
            pos = event.pos()
            self.root.insert(Point(pos.x() / width, pos.y() / height))
            self.update()
            event.accept()
            return
        self.app.quit()

    def paintEvent(self, e):
        super().paintEvent(e)
        geometry = self.geometry()

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        pen = QtGui.QPen()
        pen.setWidth(1)
        
        points = []
        stack = deque()
        stack.append(self.root.root)
        while stack:
            tmp = stack.pop()
            r = QtCore.QRect(
                (tmp.center.x - tmp.halfDimension) * geometry.width(),
                (tmp.center.y - tmp.halfDimension) * geometry.height(),
                2 * tmp.halfDimension * geometry.width(),
                2 * tmp.halfDimension * geometry.height()
            )
            if tmp.searched:
                pen.setBrush(self.searched)
            else:
                pen.setBrush(self.normal)
            painter.fillRect(r, self.fill)
            painter.setPen(pen)
            painter.drawRect(r)
            for i in tmp.children:
                if isinstance(i, Point):
                    points.append(i)
                    continue
                if isinstance(i, QuadTreeNode):
                    stack.append(i)
                    continue

        pen.setBrush(self.points)
        pen.setWidth(4)
        pen.setCapStyle(QtCore.Qt.RoundCap)
        painter.setPen(pen)
        for point in points:
            x, y = point.x, point.y
            x *= geometry.width()
            y *= geometry.height()
            painter.drawPoint(x, y)

        pen.setBrush(self.foundpoints)
        painter.setPen(pen)
        for point in self.found:
            x, y = point.x, point.y
            x *= geometry.width()
            y *= geometry.height()
            painter.drawPoint(x, y)

        if self.searching is not None:
            pen.setBrush(self.searchring)
            pen.setWidth(1)
            painter.setPen(pen)
            painter.drawEllipse(
                self.searching,
                self.radius * geometry.width(),
                self.radius * geometry.height())

if __name__ == '__main__':
    QuadTreeWindow()
