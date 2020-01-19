#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import deque
from PyQt5 import QtWidgets, QtGui, QtCore
from quadtree import QuadTree, QuadTreeNode
from point import Point

class QuadTreeWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.root = QuadTree()
        self.radius = 0.5
        self.searching = None

        self.app = QtWidgets.QApplication(sys.argv)
        super().__init__()

        self.app.setStyle("Fusion")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(20, 20, 20))
        self.app.setPalette(palette)

        self.setWindowTitle('QuadTree')
        self.resize(600, 600)
        self.show()
        # main event loop
        sys.exit(self.app.exec_())

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Q:
            self.app.quit()
        elif event.key() == QtCore.Qt.Key_A:
            self.radius *= 9 / 8
        elif event.key() == QtCore.Qt.Key_Z:
            self.radius *= 7 / 8
        event.accept()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            geometry = self.geometry()
            width, height = geometry.width(), geometry.height()
            pos = event.pos()
            self.searching = pos
            self.root.search(
                Point(pos.x() / width, pos.y() / height),
                self.radius
            )
            self.update()
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.searching = None
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
        pen.setBrush(QtGui.QColor(128, 255, 128))
        painter.setPen(pen)
        
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
                pen.setBrush(QtGui.QColor(255, 0, 0))
                # painter.fillRect(r, QtGui.QColor(255, 0, 0, 8))
            else:
                pen.setBrush(QtGui.QColor(128, 255, 128))
            painter.fillRect(r, QtGui.QColor(0, 255, 0, 8))
            painter.setPen(pen)
            painter.drawRect(r)
            for i in tmp.children:
                if isinstance(i, Point):
                    points.append(i)
                    continue
                if isinstance(i, QuadTreeNode):
                    stack.append(i)
                    continue

        pen.setBrush(QtGui.QColor(192, 255, 64))
        pen.setWidth(4)
        pen.setCapStyle(QtCore.Qt.RoundCap)
        painter.setPen(pen)
        for point in points:
            x, y = point.x, point.y
            x *= geometry.width()
            y *= geometry.height()
            painter.drawPoint(x, y)

        if self.searching is not None:
            pen.setBrush(QtGui.QColor(255, 255, 255))
            pen.setWidth(1)
            painter.setPen(pen)
            painter.drawEllipse(
                self.searching,
                self.radius,
                self.radius)

if __name__ == '__main__':
    QuadTreeWindow()
