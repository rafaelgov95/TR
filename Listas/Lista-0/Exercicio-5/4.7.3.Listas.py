# -*- coding: UTF-8 -*-
# Autor: Rafael Viana

def fprintf(file, format, *args):
    file.write(format % args)