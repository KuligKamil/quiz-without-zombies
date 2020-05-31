# quiz-without-zombies

Console game
## Notes:
### Docker
- Build an image from the Dockerfile and assign it a name.

    `$ docker build -t eg_postgresql .`
- Run the PostgreSQL server container (in the foreground):

    `$ docker run --rm -P --name pg_test eg_postgresql`
    
- Use container linking. Containers can be linked to another container’s 
ports directly using --link remote_name:local_alias in the client’s docker run. 
This sets a number of environment variables that can then be used to connect:

`$ docker run --rm -t -i --link pg_test:pg eg_postgresql bash`

`postgres@7ef98b1b7243:/$ psql -h $PG_PORT_5432_TCP_ADDR -p $PG_PORT_5432_TCP_PORT -d docker -U docker --password`

### Alembic
- When start alembic or edit:
    - `mkdir db` 
    - `cd db`
    - `alembic init alembic`
    - alembic/.env
    
        `# add your model's MetaData object here for autogenerate' support`
        
        `import sys`
        
        `sys.path = ['', '..'] + sys.path[1:]`
        
        `from db import models`
        
        `target_metadata = models.Base.metadata`
        
    - alembic/alembic.ini
    
        `sqlalchemy.url = postgres://docker:docker@localhost:32768/docker`

- What do after change models:
    - `alembic revision --autogenerate -m "what you change in model"`
    - `alembic upgrade head`  
