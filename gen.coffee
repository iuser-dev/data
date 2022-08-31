#!/usr/bin/env coffee

import fs from 'fs/promises'
import thisdir from '@rmw/thisdir'
import {join} from 'path'

DIR = thisdir import.meta

export default area_code = =>
  fp = join(DIR, 'country.cn.json')
  data = JSON.parse await fs.readFile(fp,'utf8')
  li = []
  for i of data
    li.push data[i]
  li.sort((a,b)=>a[0]-b[0])
  r = []
  for i in li
    r.push i[1]
  await fs.writeFile( join(DIR,'area_code.json'), JSON.stringify(r) )

if process.argv[1] == decodeURI (new URL(import.meta.url)).pathname
  await area_code()
