import os
import random
from datetime import datetime, timedelta

def create_commit(date):
    """
    This function creates a new commit with the provided date.
    """
    # Create a new file with the current date and commit it
    with open(f'commit_{date.strftime("%Y%m%d%H%M%S")}.txt', 'w') as file:
        file.write(date.strftime("%Y%m%d%H%M%S"))
    os.system(f'git add .')
    os.system(f'GIT_AUTHOR_DATE={date.isoformat()} GIT_COMMITTER_DATE={date.isoformat()} git commit -m "commit"')

def main():
    """
    This function generates random dates for the past year and creates commits for those dates.
    """
    # Get the current date
    current_date = datetime.now()

    # Generate commits for the past year
    for _ in range(365):
        if random.choice([True, False]):  # Randomly decide whether to commit on this day
            # Generate a random time for the commit
            hour = random.randint(0, 23)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            # Create a new date with the random time
            date = current_date.replace(hour=hour, minute=minute, second=second)
            # Create a commit for this date
            create_commit(date)

        # Move to the previous day
        current_date -= timedelta(days=1)

if __name__ == "__main__":
    main()