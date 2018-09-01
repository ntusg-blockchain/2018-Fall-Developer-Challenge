# Blockchain

## Introduction

A blockchain in the simplest of terms is literally a chain of blocks.

![BLockchain](img/simple_block_chain.png "Blockchain")
_Source_: [Imaginea](https://blog.imaginea.com/from-bitcoin-to-blockchain-to-ethereum-part-2/)

Above you can see the structure of a blockchain. Each block contains a hash of all the data contained within the previous node and its own relevant data as well.

If you are not familiar with hash pointer, please watch this [short video](https://www.coursera.org/lecture/cryptocurrency/hash-pointers-and-data-structures-EYEAo).

## The Problem

You have come up with a new 'has_' which you want to implement using blockchain technology. Unfortunately for the users (and fortunately for you) you have adopted a framework which all of the mining power is centralised.

To ensure that the mining method is fully working and deterministic you want to make sure that even if simple_coin is implemented again the hashes of the blocks are similar given that the input data does not change. You decide that the blocks should be empty to make your job easier as well.

Your goal is to implement the method in 'simple_coin.py' to verify your assumption.

NOTE: Empty blocks mean that you do not pass in any data to the block classes

## Installation

First clone this repository to your local machine using (assuming SSH key already added to your GitHub account, if not, please follow [this post](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/) to generate a new SSH key.):

```shell
git clone git@github.com:ntusg-blockchain/2018-Fall-Developer-Challenge.git
```

Make sure `python3` is properly installed on your machine, if not, please follow [this post](https://realpython.com/installing-python/) to set up.

## Project Layout

You need only to make changes to `simple_coin.py`, please make sure to familiarize yourselves with the layout of the entire directory however. The roles of the other files are as follows:

* `block.py`: contains the block object class which will act as individual blocks in the blockchain
* `blockchain.py`: contains the blockchain implementation. Make sure you familiarize yourself with how it works.
* `simple_coin.py`: contains one method which you will need to implement. the method should be able to mine the requesite number of blocks on the blockchain
* `test.py`: a script to help run all the other tests.
* `test_simple_coin.py`: testing scripts built on the `unittest` module. Each test ensures the validity of your implementation

## Running Tests

Use `python3 test.py` to run all the tests. You may add your own tests and run them with `python [filename].py`. Make sure to format tests according to the `unittest` module (take a look at the other files to see examples).

Writing your own tests is not required but highly recommended. All that matters is you pass our internal test cases.