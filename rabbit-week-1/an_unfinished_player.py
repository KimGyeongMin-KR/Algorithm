def solution(participant, completion):
    answer = ''
    un_finished = list(set(participant) - set(completion))

    participant_dict = {}

    if len(un_finished):
        answer = un_finished[0]
    else:
        for person in participant:

            if person in participant_dict:
                participant_dict[person] += 1

            else:
                participant_dict[person] = 1

        for person in completion:
            participant_dict[person] -= 1

            if participant_dict[person] == 0:
                del participant_dict[person]

        answer = list(participant_dict.keys())[0]
        
    return answer