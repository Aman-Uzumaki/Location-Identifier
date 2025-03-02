import streamlit as st
import csv
import difflib

def find_closest_match(word, options):
    matches = difflib.get_close_matches(word, options, n=1, cutoff=0.7)
    return matches[0] if matches else None

def token(word):
    lst = []
    f = open("city.csv",'r')
    reader = csv.reader(f)
    for rows in reader:
        if len(rows)>0:
            if word[:len(word)//2] in rows[4].title():
                lst.append(rows[4].title())
            if word[len(word)//2:] in rows[4].title():
                lst.append(rows[4].title())
    f.close()
    return (find_closest_match(word,lst))

common_word = {'About', 'Add', 'Also', 'Always', 'And', 
               'Angry','Are', 'Area', 'Belongs', 'B-tech', 'Btech', 'Came', 
               'Can', 'Check', 'Choice', 'City', 
               'Easily', 'Easy', 'Expect', 'Expects', 
               'Expected', 'Faculty', 'Favourite', 'From', 
               'Fast', 'Faster', 'Friend', 'Friends', 'Fun', 'Gets', 'Giet', 'Going', 'Granted', 
               'Help', 'Helps', 'Her', 'His', 'How', 'Industrial', 'Input',
               'Judge', 'Known', 'Largest', 'Learning', 'Let', 
               'Life', 'Like','Live', 'Location', 'Love', 'Loving', 
               'Make', 'Making', 'Many',
               'More', 'Most', 'Municipal', 
               'Municipality', 'Nearest', 'Need', 'Needs', 'Now', 'Output', 'Place', 
               'Planned', 'Populous', 'Proper', 'Properly', 'Railway',
               'Pursuing', 'Quite', 'Quiet', 'Reading',
               'Refer', 'Run', 'Running', 'Runs',
               'Same', 'Situated','Slow', 'Software', 'Sold', 
               'Some', 'Somehow', 'Still', 'That', 'The', 
               'Take', 'Takes', 'This', 'Those', 'Time', 'Times',
               'Tired', 'Try', 'Trying', 'User', 'Users', 'Village', 'Was', 'Were', 'Why', 'Wife', 
               'What', 'Where', 'When', 'Which', 'Who', 'Words', 'Wonder',
               'Work', 'Works','Written',
               'You', 'Your'}

additional_common_words = {
    'About', 'Above', 'Across', 'Act', 'Action', 'Activity', 'Actually', 'Add', 'Added', 'Addition',
    'Additional', 'Address', 'Admit', 'Adopt', 'Adult', 'Affect', 'After', 'Again', 'Against', 'Age',
    'Agency', 'Agent', 'Ago', 'Agree', 'Agreement', 'Ahead', 'Air', 'All', 'Allow', 'Almost',
    'Alone', 'Along', 'Already', 'Also', 'Alter', 'Alternative', 'Although', 'Always', 'American',
    'Among', 'Amount', 'Analysis', 'And', 'Animal', 'Another', 'Answer', 'Any', 'Anyone', 'Anything',
    'Appear', 'Apply', 'Approach', 'Area', 'Argue', 'Arm', 'Around', 'Arrive', 'Art', 'Article',
    'Artist', 'As', 'Ask', 'Aspect', 'Assume', 'At', 'Attack', 'Attention', 'Attorney', 'Audience',
    'Author', 'Authority', 'Available', 'Avoid', 'Away', 'Baby', 'Back', 'Bad', 'Bag', 'Ball', 'Bank',
    'Bar', 'Base', 'Be', 'Beat', 'Beautiful', 'Because', 'Become', 'Bed', 'Before', 'Begin', 'Behavior',
    'Behind', 'Believe', 'Benefit', 'Best', 'Better', 'Between', 'Beyond', 'Big', 'Bill', 'Billion',
    'Bit', 'Black', 'Blood', 'Blue', 'Board', 'Body', 'Book', 'Born', 'Both', 'Box', 'Boy', 'Break',
    'Bring', 'Brother', 'Budget', 'Build', 'Building', 'Business', 'But', 'Buy', 'By', 'Call', 'Camera',
    'Campaign', 'Can', 'Cancer', 'Candidate', 'Capital', 'Car', 'Card', 'Care', 'Career', 'Carry', 'Case',
    'Catch', 'Cause', 'Cell', 'Center', 'Central', 'Century', 'Certain', 'Certainly', 'Chair', 'Challenge',
    'Chance', 'Change', 'Character', 'Charge', 'Check', 'Child', 'Choice', 'Choose', 'Church', 'Citizen',
    'City', 'Civil', 'Claim', 'Class', 'Clear', 'Clearly', 'Close', 'Coach', 'Cold', 'Collection', 'College',
    'Color', 'Come', 'Commercial', 'Common', 'Community', 'Company', 'Compare', 'Computer', 'Concern',
    'Condition', 'Conference', 'Congress', 'Consider', 'Consumer', 'Contain', 'Continue', 'Control',
    'Cost', 'Could', 'Country', 'Couple', 'Course', 'Court', 'Cover', 'Create', 'Crime', 'Cultural',
    'Culture', 'Cup', 'Current', 'Customer', 'Cut', 'Dark', 'Data', 'Daughter', 'Day', 'Dead', 'Deal',
    'Dealer', 'Dear', 'Death', 'Debate', 'Decade', 'Decide', 'Decision', 'Deep', 'Defense', 'Degree',
    'Democrat', 'Democratic', 'Describe', 'Design', 'Despite', 'Detail', 'Determine', 'Develop',
    'Development', 'Die', 'Difference', 'Different', 'Difficult', 'Dinner', 'Direction', 'Director',
    'Discover', 'Discuss', 'Discussion', 'Disease', 'Do', 'Doctor', 'Dog', 'Door', 'Down', 'Draw', 'Dream',
    'Drive', 'Drop', 'Drug', 'During', 'Each', 'Early', 'East', 'Easy', 'Eat', 'Economic', 'Economy',
    'Edge', 'Education', 'Effect', 'Effort', 'Eight', 'Either', 'Election', 'Else', 'Employee', 'End',
    'Energy', 'Enjoy', 'Enough', 'Enter', 'Entire', 'Environment', 'Environmental', 'Especially', 'Establish',
    'Even', 'Evening', 'Event', 'Ever', 'Every', 'Everybody', 'Everyone', 'Everything', 'Evidence', 'Exactly',
    'Example', 'Executive', 'Exist', 'Expect', 'Experience', 'Expert', 'Explain', 'Eye', 'Face', 'Fact',
    'Factor', 'Fail', 'Fall', 'Family', 'Far', 'Fast', 'Father', 'Fear', 'Federal', 'Feel', 'Feeling', 'Few',
    'Field', 'Fight', 'Figure', 'Fill', 'Film', 'Final', 'Finally', 'Financial', 'Find', 'Fine', 'Finger',
    'Finish', 'Fire', 'Firm', 'First', 'Fish', 'Five', 'Floor', 'Fly', 'Focus', 'Follow', 'Food', 'Foot',
    'For', 'Force', 'Foreign', 'Forget', 'Form', 'Former', 'Forward', 'Four', 'Free', 'Friend', 'From', 'Front',
    'Full', 'Fund', 'Future', 'Game', 'Garden', 'Gas', 'General', 'Generation', 'Get', 'Girl', 'Give', 'Glass',
    'Go', 'Goal', 'Good', 'Government', 'Great', 'Green', 'Ground', 'Group', 'Grow', 'Growth', 'Guess', 'Gun',
    'Guy', 'Hair', 'Half', 'Hand', 'Hang', 'Happen', 'Happy', 'Hard', 'Have', 'He', 'Head', 'Health', 'Hear',
    'Heart', 'Heat', 'Heavy', 'Help', 'Her', 'Here', 'Herself', 'High', 'Him', 'Himself', 'His', 'History', 'Hit',
    'Hold', 'Home', 'Hope', 'Hospital', 'Hot', 'Hotel', 'Hour', 'House', 'How', 'However', 'Huge', 'Human',
    'Hundred', 'Husband', 'I', 'Idea', 'Identify', 'If', 'Image', 'Imagine', 'Impact', 'Important', 'Improve',
    'In', 'Include', 'Including', 'Increase', 'Indeed', 'Indicate', 'Individual', 'Industry', 'Information',
    'Inside', 'Instead', 'Institution', 'Interest', 'Interesting', 'International', 'Interview', 'Into',
    'Investment', 'Involve', 'Issue', 'It', 'Item', 'Its', 'Itself', 'Job', 'Join', 'Just', 'Keep', 'Key', 'Kid',
    'Kill', 'Kind', 'Kitchen', 'Know', 'Knowledge', 'Land', 'Language', 'Large', 'Last', 'Late', 'Later', 'Laugh',
    'Law', 'Lawyer', 'Lay', 'Lead', 'Leader', 'Learn', 'Least', 'Leave', 'Left', 'Leg', 'Legal', 'Less', 'Let',
    'Letter', 'Level', 'Lie', 'Life', 'Light', 'Like', 'Likely', 'Line', 'List', 'Listen', 'Little', 'Live',
    'Local', 'Long', 'Look', 'Lose', 'Loss', 'Lot', 'Love', 'Low', 'Machine', 'Magazine', 'Main', 'Maintain',
    'Major', 'Majority', 'Make', 'Man', 'Manage', 'Management', 'Manager', 'Many', 'Market', 'Marriage', 'Material',
    'Matter', 'May', 'Maybe', 'Me', 'Mean', 'Measure', 'Media', 'Medical', 'Meet', 'Meeting', 'Member', 'Memory',
    'Mention', 'Message', 'Method', 'Middle', 'Might', 'Military', 'Million', 'Mind', 'Minute', 'Miss', 'Mission',
    'Model', 'Modern', 'Moment', 'Money', 'Month', 'More', 'Morning', 'Most', 'Mother', 'Mouth', 'Move', 'Movement',
    'Movie', 'Mr', 'Mrs', 'Much', 'Music', 'Must', 'My', 'Myself', 'Name', 'Nation', 'National', 'Natural', 'Nature',
    'Near', 'Nearly', 'Necessary', 'Need', 'Network', 'Never', 'New', 'News', 'Newspaper', 'Next', 'Nice', 'Night',
    'No', 'None', 'Nor', 'North', 'Not', 'Note', 'Nothing', 'Notice', 'Now', 'Number', 'Occur', 'Of', 'Off', 'Offer',
    'Office', 'Officer', 'Official', 'Often', 'Oh', 'Oil', 'Ok', 'Old', 'On', 'Once', 'One', 'Only', 'Onto', 'Open',
    'Operation', 'Opportunity', 'Option', 'Or', 'Order', 'Organization', 'Other', 'Others', 'Our', 'Out', 'Outside',
    'Over', 'Own', 'Owner', 'Page', 'Pain', 'Painting', 'Paper', 'Parent', 'Part', 'Participant', 'Particular', 'Particularly',
    'Partner', 'Party', 'Pass', 'Past', 'Patient', 'Pattern', 'Pay', 'Peace', 'People', 'Per', 'Perform', 'Performance',
    'Perhaps', 'Period', 'Person', 'Personal', 'Phone', 'Physical', 'Pick', 'Picture', 'Piece', 'Place', 'Plan', 'Plant',
    'Play', 'Player', 'PM', 'Point', 'Police', 'Policy', 'Political', 'Politics', 'Poor', 'Popular', 'Population', 'Position',
    'Positive', 'Possible', 'Power', 'Practice', 'Prepare', 'Present', 'President', 'Pressure', 'Pretty', 'Prevent', 'Price',
    'Private', 'Probably', 'Problem', 'Process', 'Produce', 'Product', 'Production', 'Professional', 'Professor', 'Program',
    'Project', 'Property', 'Protect', 'Prove', 'Provide', 'Public', 'Pull', 'Purpose', 'Push', 'Put', 'Quality', 'Question',
    'Quickly', 'Quite', 'Race', 'Radio', 'Raise', 'Range', 'Rate', 'Rather', 'Reach', 'Read', 'Ready', 'Real', 'Reality', 'Realize',
    'Really', 'Reason', 'Receive', 'Recent', 'Recently', 'Recognize', 'Record', 'Red', 'Reduce', 'Reflect', 'Region', 'Relate',
    'Relationship', 'Religious', 'Remain', 'Remember', 'Remove', 'Report', 'Represent', 'Republican', 'Require', 'Research',
    'Resource', 'Respond', 'Response', 'Responsibility', 'Rest', 'Result', 'Return', 'Reveal', 'Rich', 'Right', 'Rise', 'Risk',
    'Road', 'Rock', 'Role', 'Room', 'Rule', 'Run', 'Safe', 'Same', 'Save', 'Say', 'Scene', 'School', 'Science', 'Scientist', 'Score',
    'Sea', 'Season', 'Seat', 'Second', 'Section', 'Security', 'See', 'Seek', 'Seem', 'Sell', 'Send', 'Senior', 'Sense', 'Series',
    'Serious', 'Serve', 'Service', 'Set', 'Seven', 'Several', 'Sex', 'Sexual', 'Shake', 'Share', 'She', 'Shoot', 'Short', 'Shot',
    'Should', 'Shoulder', 'Show', 'Side', 'Sign', 'Significant', 'Similar', 'Simple', 'Simply', 'Since', 'Sing', 'Single', 'Sister',
    'Sit', 'Site', 'Situation', 'Six', 'Size', 'Skill', 'Skin', 'Small', 'Smile', 'So', 'Social', 'Society', 'Soldier', 'Some',
    'Somebody', 'Someone', 'Something', 'Sometimes', 'Son', 'Song', 'Soon', 'Sort', 'Sound', 'Source', 'South', 'Southern', 'Space',
    'Speak', 'Special', 'Specific', 'Speech', 'Spend', 'Sport', 'Spring', 'Staff', 'Stage', 'Stand', 'Standard', 'Star', 'Start',
    'State', 'Statement', 'Station', 'Stay', 'Step', 'Still', 'Stock', 'Stop', 'Store', 'Story', 'Strategy', 'Street', 'Strong',
    'Structure', 'Student', 'Study', 'Stuff', 'Style', 'Subject', 'Success', 'Successful', 'Such', 'Suddenly', 'Suffer', 'Suggest',
    'Summer', 'Support', 'Sure', 'Surface', 'System', 'Table', 'Take', 'Talk', 'Task', 'Tax', 'Teach', 'Teacher', 'Team', 'Technology',
    'Television', 'Tell', 'Ten', 'Tend', 'Term', 'Test', 'Than', 'Thank', 'That', 'The', 'Their', 'Them', 'Themselves', 'Then', 'Theory',
    'There', 'These', 'They', 'Thing', 'Think', 'Third', 'This', 'Those', 'Though', 'Thought', 'Thousand', 'Threat', 'Three', 'Through',
    'Throughout', 'Throw', 'Thus', 'Time', 'To', 'Today', 'Together', 'Tonight', 'Too', 'Top', 'Total', 'Tough', 'Toward', 'Town', 'Trade',
    'Traditional', 'Training', 'Travel', 'Treat', 'Treatment', 'Tree', 'Trial', 'Trip', 'Trouble', 'True', 'Truth', 'Try', 'Turn', 'TV',
    'Two', 'Type', 'Under', 'Understand', 'Unit', 'Until', 'Up', 'Upon', 'Us', 'Use', 'Usually', 'Value', 'Various', 'Very', 'Victim', 'View',
    'Violence', 'Visit', 'Voice', 'Vote', 'Wait', 'Walk', 'Wall', 'Want', 'War', 'Watch', 'Water', 'Way', 'We', 'Weapon', 'Wear', 'Week', 'Weight',
    'Well', 'West', 'Western', 'What', 'Whatever', 'When', 'Where', 'Whether', 'Which', 'While', 'White', 'Who', 'Whole', 'Whom', 'Whose', 'Why',
    'Wide', 'Wife', 'Will', 'Win', 'Wind', 'Window', 'Wish', 'With', 'Within', 'Without', 'Woman', 'Wonder', 'Word', 'Work', 'Worker', 'World',
    'Worry', 'Would', 'Write', 'Writer', 'Wrong', 'Yard', 'Yeah', 'Year', 'Yes', 'Yet', 'You', 'Young', 'Your', 'Yourself'
}

common_word.update(additional_common_words)

st.title("Enter the sentence to detect location: ")
sentence = list((st.text_input("Enter your sentence: ").title()).split())
if st.button('Check'):
    city = []
    for i in sentence:
        if len(i) >= 3 and i not in common_word:
            a = token(i)
            if a != None:
                f = open('city.csv','r')
                reader = csv.reader(f)
                for rows in reader:
                    if rows[4] == a:
                        city.append(rows)
                f.close()
 
    if len(city) != 0:
        st.text("The following locations were detected:\n")
        common = city[0][4]
        st.text("Set 1:")
        set1 = 1
        counter = 1
        for i in city:
            if i[4] != common:
                common = i[4]
                counter = 1
                set1 += 1
                st.text("")
                st.text(f"Set {set1}:")
            st.text(f"{counter}. {i[4]}, {i[1]}, {i[0]}.")
            counter += 1
    else:
        st.text("No location were detected.")