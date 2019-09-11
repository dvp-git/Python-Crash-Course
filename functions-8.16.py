# Exercise 8.16 Imports

import printing_funtions
from printing_funtions import show_completed_models
from printing_funtions import show_completed_models as scm
import printing_funtions as pf
from printing_funtions import *


models = ['car','building','bus','plane','bike','table']

## import printing_funtions

printing_funtions.show_completed_models(models)


## from printing_funtions import show_completed_models

show_completed_models(models)

## from printing_funtions import show_completed_models as scm

scm(models)

## import printing_funtions as pf
pf.show_completed_models(models)

## from printing_funtions import *
show_completed_models(models)


