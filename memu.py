from notebook import Note,NoteBook
import sys
class Memu(object):
    def __init__(self):
        self.notebook = NoteBook()
        self.choices = {
            "1":self.show_notes,
            "2":self.search_notes,
            "3":self.add_note,
            "4":self.modify_note,
            "5":self.quit
        }

    def display_memu(self):
        print ("""
        Notebook Menu

        1.Show all Notes
        2.Search Notes
        3.Add Note
        4.Modify Note
        5.Quit
        """)
    def run(self):
        while True:
            self.display_memu()
            choice = raw_input("Enter an option:")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print "{0} is not a valid choice".format(choice)
    def show_notes(self,notes = None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print ("{0}:{1}\n{2}".format(note.id,note.tags,note.memo))
    def search_notes(self):
        filter = raw_input("Search for:")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = raw_input("Enter a memo:")
        self.notebook.new_note(memo)
        print "Your note has been added."
    def modify_note(self):
        id = raw_input("Enter a note id:")
        memo = raw_input("Enter a memo:")
        tags = raw_input("Enter tags:")
        if memo:
            self.notebook.modify_note(id,memo)
        if tags:
            self.notebook.modify_tags(id,tags)

    def quit(self):
        print "Thank you for using your notebook today."
        sys.exit(0)


if __name__=="__main__":
    Memu().run()
