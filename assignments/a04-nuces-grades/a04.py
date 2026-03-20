## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####
def get_grade(score):
    match score:
        case _ if 90 <= score <= 100:
            return 'A+'
        case _ if 86<=score <90:
            return 'A'
        case _ if 82<=score<86:
            return 'A-'
        case _ if 78<=score<82:
            return 'B+'
        case _ if 74<=score<78:
            return 'B'
        case _ if 70<=score<74:
            return 'B-'
        case _ if 66<=score<70:
            return 'C+'
        case _ if 62<=score<66:
            return 'C'
        case _ if 58<=score<62:
            return 'C-'
        case _ if 54<=score<58:
            return 'D+'
        case _ if 50<=score<54:
            return 'D'
        case _ if 0<=score<50:
            return 'F'
#### End OF MARKER

#### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ####

#### End OF MARKER




if __name__ == '__main__':
    print (get_grade(50))
    print (calculate_sgpa('A', 'B', 'nothing'))
