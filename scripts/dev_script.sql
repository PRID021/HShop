-- Insert 20 realistic questions into the "app_question" table
DO $$ 
BEGIN
    INSERT INTO app_question (question_text, pub_date)
    VALUES ('What is the capital of France?', NOW());

    INSERT INTO app_question (question_text, pub_date)
    VALUES ('Which planet is known as the Red Planet?', NOW());

    INSERT INTO app_question (question_text, pub_date)
    VALUES ('Who wrote "Romeo and Juliet"?', NOW());

    INSERT INTO app_question (question_text, pub_date)
    VALUES ('What is the square root of 64?', NOW());

    INSERT INTO app_question (question_text, pub_date)
    VALUES ('Which element has the chemical symbol O?', NOW());

    INSERT INTO app_question (question_text, pub_date)
    VALUES ('In which year did World War II end?', NOW());

    INSERT INTO app_question (question_text, pub_date)
    VALUES ('What is the largest mammal?', NOW());

    INSERT INTO app_question (question_text, pub_date)
    VALUES ('How many continents are there?', NOW());

    INSERT INTO app_question (question_text, pub_date)
    VALUES ('What is the boiling point of water in Celsius?', NOW());

    INSERT INTO app_question (question_text, pub_date)
    VALUES ('Who painted the Mona Lisa?', NOW());

    INSERT INTO app_question (question_text, pub_date)
    VALUES ('Which country is known as the Land of the Rising Sun?', NOW());

    INSERT INTO app_question (question_text, pub_date)
    VALUES ('What is the largest planet in our solar system?', NOW());

    INSERT INTO app_question (question_text, pub_date)
    VALUES ('Which country won the FIFA World Cup in 2018?', NOW());

    INSERT INTO app_question (question_text, pub_date)
    VALUES ('What is the chemical formula for water?', NOW());

    INSERT INTO app_question (question_text, pub_date)
    VALUES ('Who developed the theory of relativity?', NOW());

    INSERT INTO app_question (question_text, pub_date)
    VALUES ('What is the speed of light?', NOW());

    INSERT INTO app_question (question_text, pub_date)
    VALUES ('Which organ pumps blood throughout the body?', NOW());

    INSERT INTO app_question (question_text, pub_date)
    VALUES ('What is the tallest mountain in the world?', NOW());

    INSERT INTO app_question (question_text, pub_date)
    VALUES ('What is the hardest natural substance on Earth?', NOW());

    INSERT INTO app_question (question_text, pub_date)
    VALUES ('What is the freezing point of water in Fahrenheit?', NOW());
END $$;

-- Insert 3 realistic answers for each question into the "app_choice" table
DO $$ 
DECLARE
    question_id INT;
BEGIN
    FOR question_id IN (SELECT id FROM app_question) LOOP
        -- Answers for 'What is the capital of France?'
        IF question_id = 1 THEN
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Paris', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'London', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Berlin', 0);
        -- Answers for 'Which planet is known as the Red Planet?'
        ELSIF question_id = 2 THEN
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Mars', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Venus', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Jupiter', 0);
        -- Answers for 'Who wrote "Romeo and Juliet"?'
        ELSIF question_id = 3 THEN
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'William Shakespeare', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Charles Dickens', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Jane Austen', 0);
        -- Continue similar patterns for other questions
        ELSIF question_id = 4 THEN
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, '8', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, '7', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, '9', 0);
        ELSIF question_id = 5 THEN
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Oxygen', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Hydrogen', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Carbon', 0);
        ELSIF question_id = 6 THEN
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, '1945', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, '1939', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, '1950', 0);
        -- Answers for 'What is the largest mammal?'
        ELSIF question_id = 7 THEN
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Blue Whale', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Elephant', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Giraffe', 0);
        -- Answers for 'How many continents are there?'
        ELSIF question_id = 8 THEN
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, '7', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, '6', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, '8', 0);
        -- Answers for 'What is the boiling point of water in Celsius?'
        ELSIF question_id = 9 THEN
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, '100°C', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, '90°C', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, '110°C', 0);
        -- Answers for 'Who painted the Mona Lisa?'
        ELSIF question_id = 10 THEN
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Leonardo da Vinci', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Michelangelo', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Vincent van Gogh', 0);
        -- Answers for 'Which country is known as the Land of the Rising Sun?'
        ELSIF question_id = 11 THEN
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Japan', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'China', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'South Korea', 0);
        -- Answers for 'What is the largest planet in our solar system?'
        ELSIF question_id = 12 THEN
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Jupiter', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Saturn', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Earth', 0);
        -- Answers for 'Which country won the FIFA World Cup in 2018?'
        ELSIF question_id = 13 THEN
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'France', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Brazil', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Germany', 0);
        -- Answers for 'What is the chemical formula for water?'
        ELSIF question_id = 14 THEN
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'H2O', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'CO2', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'O2', 0);
        -- Answers for 'Who developed the theory of relativity?'
        ELSIF question_id = 15 THEN
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Albert Einstein', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Isaac Newton', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Nikola Tesla', 0);
        -- Answers for 'What is the speed of light?'
        ELSIF question_id = 16 THEN
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, '299,792,458 meters per second', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, '150,000,000 meters per second', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, '100,000,000 meters per second', 0);
        -- Answers for 'Which organ pumps blood throughout the body?'
        ELSIF question_id = 17 THEN
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Heart', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Lungs', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Kidneys', 0);
        -- Answers for 'What is the tallest mountain in the world?'
        ELSIF question_id = 18 THEN
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Mount Everest', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'K2', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Kangchenjunga', 0);
        -- Answers for 'What is the hardest natural substance on Earth?'
        ELSIF question_id = 19 THEN
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Diamond', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Gold', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, 'Iron', 0);
        -- Answers for 'What is the freezing point of water in Fahrenheit?'
        ELSIF question_id = 20 THEN
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, '32°F', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, '0°F', 0);
            INSERT INTO app_choice (question_id, choice_text, votes) VALUES (question_id, '100°F', 0);            
        END IF;
    END LOOP;
END $$;
