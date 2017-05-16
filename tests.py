import unittest



class TestRoom(unittest.TestCase)

    def setUp(self):
        self.persons = [
            Fellow("Alex Manthi", "Y", gender="M"),
            Fellow("Rose Maina", "Y", gender="F"),
            Fellow("Jackline Keli", "Y", gender="F"),
            Fellow("David Njenga", "Y", gender="M"),
            Staff("Murugi Kamau"),
            Staff("Ella Nduta"), 

    #tests that the persons should have a name if not an error occurs      
    def test_instance_must_have_name(self):
        with self.assertRaises(TypeError):
        Room()

    #Test raises an error if the name provided is not a string
    def test_raises_error_if_name_is_not_string(self):
        with self.assertRaises(TypeError):
        Room(302)

    #Test adds an new occupant to the Occupant's list
    def test_add_occupant_adds_to_occupants_list(self):
        room = Room("Aberdare")
        room.add_occupant1(Fellow("Joe Tess", "Y"))
        self.assertEqual(len(room.occupants), 1)

    #Test makes sure that the number of occupants is not excess
    def test_added_occupant_never_exceeds_max_occpants(self):
        room = LivingSpace("Aberdare")
        for person in self.persons:
            room.add_occupant(person)
        self.assertEqual(len(room.occupants), 4)

    def test_add_occupant_adds_only_person_instances(self):
        room = Room("Aberdare")
        self.assertFalse(room.add_occupant(None))

    def test_add_occupants_accepts_only_lists(self):
        room = Room("Suswa")
        self.assertFalse(room.add_occupants({}))

    def test_new_room_name(self):
        self.assertEqual(self.room.name, 'Elgon')

    def test_new_room_members(self):
        self.assertEqual(self.room.members, {})




class TestOfficeSpace(unittest.TestCase):

    def setUp(self):
        self.room = OfficeSpace("Elgon")

    def test_raises_error_if_occupant_role_is_not_valid(self):
        with self.assertRaises(ValueError):
            OfficeSpace("Rose Maina", occupant_role="Fellow")

    def test_repr_returns_correct_values(self):
        self.room = OfficeSpace("Elgon")
        self.assertEqual(str(self.room), "Elgon (OFFICE)")

        # test again with occupant_role specified:
        self.room = OfficeSpace("Elgon", occupant_role="STAFF")
        self.assertEqual(str(self.room), "Elgon (OFFICE STAFF)")





class LivingSpaceTests(unittest.TestCase):

    def setUp(self):
        self.room = LivingSpace("Aberdare")

    def test_raises_error_if_occupant_gender_is_not_valid(self):
        with self.assertRaises(ValueError):
            LivingSpace("Aberdare", occupant_gender="F")

    def test_repr_returns_correct_values(self):
        self.room = LivingSpace("Aberdare")
        self.assertEqual(str(self.room), "Aberdare (LIVING)")
        
        # test again with occupant_role specified:
        self.room = LivingSpace("Aberdare", occupant_gender="M")
        self.assertEqual(str(self.room), "Aberdare (LIVING M)")





if __name__ == '__main__':
    unittest.main()





































    def test_check_gender(self):
        person_gender = Person()
        gender = person_gender.check_gender('Male' or 'Female' or 'Other')
        self.assertIsInstance(gender)


        self.person_name = person_name()
        self.gender = 'Male' or 'Female' or 'Other'



class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person()
        pass