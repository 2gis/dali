#!/usr/bin/env bash

thrift -out backend/thrift_py --gen py config/dali.thrift
