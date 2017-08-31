# -*- coding: utf-8 -*-
def fprintf(file, format, *args):
    file.write(format % args)