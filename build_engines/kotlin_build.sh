#!/bin/bash
kotlinc kotlin/*.kt tests/*.kt -include-runtime -d test.jar
kotlin -cp test.jar:junit-4.13.2.jar org.junit.runner.JUnitCore DataProcessorTest
