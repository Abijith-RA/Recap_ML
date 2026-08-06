{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "0a678915-79f6-4d02-abc5-a44f6b086cec",
   "metadata": {
    "deletable": true,
    "editable": true,
    "slideshow": {
     "slide_type": ""
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "40\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "array = np.array([10, 20, 30, 40])\n",
    "\n",
    "print(array[0])\n",
    "print(array[-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6d53a8a2-75e5-4da2-bd7d-cb117d0d96bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5 6]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3, 4, 5, 6])\n",
    "\n",
    "print(a[(a >= 3) | (a < 4)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "42d497bb-80e2-49cc-afad-ad36991c46df",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2 4 6]\n"
     ]
    }
   ],
   "source": [
    "evens = a[a % 2 == 0]\n",
    "\n",
    "print(evens)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
