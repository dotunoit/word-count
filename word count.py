{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef5ed251",
   "metadata": {},
   "outputs": [],
   "source": [
    "#The 2 variables to sort the sentence into digit & letters \n",
    "digits = 0\n",
    "letters = 0\n",
    "\n",
    "#Accepting Sentence to be analysed\n",
    "sentence = input(\"Please enter a sentence: \")\n",
    "\n",
    "# For loop to count through the sentence\n",
    "for char in sentence:\n",
    "    if char.isalpha():\n",
    "        letters += 1\n",
    "    if char.isdigit():\n",
    "        digits+= 1\n",
    "#Outputs \n",
    "print(\"LETTERS:\", letters)\n",
    "print(\"DIGITS:\", digits) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "729ce1b0",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
