import datetime

last_id = 0
class Note(object):
    def __init__(self,memo,tags= ""):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id +=1
        self.id = last_id




    def match(self,filter):
        return filter in self.memo or filter in self.tags


class NoteBook(object):
    def __init__(self):
        self.notes =[]

    def new_note(self,memo,tags=""):
        self.notes.append(Note(memo,tags))
    def modify_note(self,note_id,memo):
        note = self._finde_note(note_id)
        if note:
            note.memo = memo
            return True
        return False
    def modify_tags(self,note_id,tags):
        note = self._finde_note(note_id)
        note.tags = tags

    def search(self,filter):
        return [note for note in self.notes if note.match(filter)]
    def _finde_note(self,note_id):
        for eachnote in self.notes:
            if str(eachnote.id) ==str(note_id):
                return eachnote
        return None


