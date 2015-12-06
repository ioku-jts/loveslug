#########################################################################
## Define your tables below; for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

#Additional info to show on Personal Profile
db.define_table('person',
                Field('image', 'upload'),
                Field('about_me', 'text'),
                Field('interests', 'text'),
                Field('major', 'string'),
                Field('college', requires=IS_IN_SET(['Nine', 'Ten',
                                                    'Crown', 'Merrill',
                                                    'Stevenson', 'Cowell',
                                                    'Porter', 'Kresge',
                                                    'Oakes','Eight',
                                                    'Off Campus'])),
               )

# Chat Table
# Will be used to hold chat messages for IMs.
# - Cole
db.define_table('chat',
                Field('sender', requires=IS_NOT_EMPTY()),   # User who sent
                Field('receiver', requires=IS_NOT_EMPTY()), # User who it's to'
                Field('body', requires=IS_NOT_EMPTY()),     # Text in chat message
                Field('seen', requires=IS_NOT_EMPTY()),     # Has it been seen?
                Field('sent', requires=IS_NOT_EMPTY()),# Time it was sent
                )

# Message Table
# Will be used to hold e-mails between two users.
# - Cole
db.define_table('email',
                Field('sender', requires=IS_NOT_EMPTY()),   # User who sent
                Field('receiver', requires=IS_NOT_EMPTY()), # User who it's to'
                Field('body', requires=IS_NOT_EMPTY()),     # Text in chat message
                Field('subject', requires=IS_NOT_EMPTY()),  # Subject of message
                Field('seen', requires=IS_NOT_EMPTY()),     # Has it been seen?
                Field('sent', requires=IS_NOT_EMPTY()),# Time it was sent
                )
