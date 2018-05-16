# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 2018/5/16 18:50
    @Name: page_replacement
    @Project: neu_curriculum
"""
import fifo
import lru
import rand_page

series_size = 20
random_size = 7

if __name__ == "__main__":
    access_series = rand_page.random_list(0, random_size, series_size)
    fifo.fifo(3, access_series)
    lru.lru(access_series)
