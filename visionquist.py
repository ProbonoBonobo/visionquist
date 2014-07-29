import random

#some of these are norquisms. some are ayn randisms. add more. also figure out how to enclose them in actual quotes 
terminal_quotes = list(['I have a pen and phone.', 
	'``There will be no earmarks.``',
	'``That government is best which governs least.``',
	'``Wars end.``',
	'``Spending is what politicians do instead of caring.``',
	'``I want to raise taxes to pay for X.``',
	'``When a government is just, the taxes are few.``',
	'``Forever are the debts we pay to be entrusted, in turn, to those who know what`s best for us.``',
	'``Never have so many felt so powerful and so weak all at once.``',
	'``Achievement of your happiness is the only moral goal in life.``',
	'``A creative man is motivated by the desire to achieve, not by the desire to beat others.``',
	'``Money is only a tool. It will take you wherever you wish, but it will not replace you as the driver.``',
	'``Money is the barometer of a society`s virtue.``',
	]
	)

#not currently being used
confrontational_questions = list(['Where is your sister?',
	'Why a federal gas tax at all?',
	])

#not currently being used
epithets = list(['stimulus',
	'single payer',
	'income inequality',
	'recovery'
	'tsunami'
	'war on poverty'
	])

verb_phrases = list(['has agreed:',
	'told me that',

	'is certain of one thing:',
	'disappeared into a cloud that said:',
	'hit me up for small talk. ', 
	'on the arrival of my daughter:',
	'has said that',
	'told me today that',
	'would like you to believe that',
	'doubts that',
	'convinced me today:',
	'isn`t sure that',
	'challenged me to accept that',
	'at 9am today:',
	'as a breeze went by:',
	'spoke the following:',
	'purred:',
	'coughed in my ear,',
	'impressed me when he said,',
	'when I said I was losing faith:',
	'is certain that',
	'when the lights went out:'
	])

#terminal commentary is 99% verbatim norquisms from his twitter feed
terminal_commentary = list(['(Not a bad guess.)',
	'Aspen, Colorado is lovely.',
	'Happy Cost of Government Day, America!',
	'Not much to see.',
	'The mountains block out the view.',
	'Ok so far',
	'no blood on the floor',
	'How government starts?',
	'Paging Bill and Hillary',
	'Phone optional.',
	'UBER is the future.',
	'Choose where you live.',
	'This book is on schedule.',
	'Explains much.',
	'Why a federal gas tax at all?',
	'True.',
	'Tipping point.',
	'Pockets full.',
	'I`m soaking wet.',
	'I peed.',
	'Wow!',
	'I was gruntled.',
	'New rule.',
	'I could have saved 75 cents.',
	'Just maybe the state can be saved.',
	'(That is our job.)',
	'Mom, please hurry home.',
	'I wrote my own joke.',
	'I now believe in reincarnation.'
	])

animist_noun_phrase = list(['An amicable sagebrush',
	'My depraved rock mascot',
	'A rugged seafarer',
	'Some new red bee',
	'A bird that was on fire',
	'A representative of the foxes',
	'Some gallant terrapin',
	'An osprey in an unusual place',
	'The spritely gentleman with the lace stockings',
	'A morbid junebug',
	'That wise ibex on the butte',
	'The extant shell of a bird-eaten crustacean',
	'Some green peas in a sandwich bag',
	'The clam I ate in a Winnebago',
	'That green cloud in my dream',
	'An orange candy bag',
	'A black ocean full of spiders',
	'A cormorant`s tumescent belly',
	'This Saguaro cactus made of dreams',
	'My red boulder made of clay',
	'A fossilized stump of a cypress tree',
	'That lady with the beet-red hair',
	'A smug ladybug guarding a pile of eggs',
	'A morbidly obese aphid',
	'That sheet of boiling sand',
	'A blanket in a cozy situation',
	'Your sand dune',
	'That ant',
	'The disquietude of bees',
	'A carnival barker filled with worms',
	'A wise-assed fruit bat',
	'A delirious stranger',
	'My potato chip',
	'My beer can',
	'My female alter-ego',
	'My child'
	]
	)
count = range(1,100)


# to do: satisfy the 140-character constraint for tweetability
for quote in count:
	print random.choice(animist_noun_phrase), random.choice(past_predicates), random.choice(terminal_quotes), random.choice(terminal_commentary)