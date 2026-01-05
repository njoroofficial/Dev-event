from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


supabase_url = "postgresql://postgres.wwjayfgmjugkzblcpkll:@Moses12960@@aws-1-eu-west-1.pooler.supabase.com:5432/postgres"
engine = create_engine(supabase_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)






