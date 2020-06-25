if __name__ == '__main__':
    print('And then he turns to Scarlett and says, "Frankly my dear, I don\'t give a damn."')
   
    print('I\'m gonna make him an offer he can\'t refuse.')
   
    print("""To be, or not to be, that is the question:
Whether \'tis nobler in the mind to suffer
The slings and arrows or outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them.""")
  
    print('It is a truth universally acknowledged, \
that a single man in possession of a good fortune, \
must be in want of a wife.')

    george_orwell = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    print(len(george_orwell))

    chanel_1 = 'The most courageous act is still to think for yourself. '
    chanel_2 = 'Aloud.'
    print(chanel_1 + chanel_2)
    
    einstein_1 = 'I have no special talent.'
    einstein_2 = 'I am only passionately curious.'
    print(einstein_1 + ' ' + einstein_2)

    print('nerf herder'[:4])

    'Jalin'.lower()
    'Obi-Wan'.lower()
    'Darth Maul'.lower()
    'Rex'.lower()

    'Jalin'.upper()
    'Obi-Wan'.upper()
    'Rex'.upper()

    ' Ezra Bridger is my apprentice! '.strip()

    solo = 'Han Solo shot first'
    solo.replace('Han', 'Ben').replace('shot', 'stabbed')

    dathomir = 'Dathomir is the home planet of the Night Sisters'
    word = 'Night'
    night_start = dathomir.find(word)
    night_end = night_start + len(word) - 1
    print(f'Start: {night_start} End: {night_end}')
    print(dathomir[night_start:night_end + 1])

    kessel_run = 'The {ship} can make the Kessel Run in less than {distance} parsecs'

    ship = 'Millennium Falcon'
    distance = 12
    kessel_run.format(
        ship = ship,
        distance = distance)

    ship = 'Ghost'
    distance = 20
    f'The {ship} can make the Kessel Run in less than {distance} parsecs'
