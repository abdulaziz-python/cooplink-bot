import asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from config import DATABASE_URL

ASYNC_DATABASE_URL = DATABASE_URL.replace('postgresql://', 'postgresql+asyncpg://')

async def migrate_database():
    engine = create_async_engine(ASYNC_DATABASE_URL)
    
    async with engine.begin() as conn:
        # Drop foreign key constraint first
        await conn.execute(text("ALTER TABLE listings DROP CONSTRAINT IF EXISTS listings_user_id_fkey"))
        
        # Alter column types
        await conn.execute(text("ALTER TABLE users ALTER COLUMN id TYPE BIGINT"))
        await conn.execute(text("ALTER TABLE listings ALTER COLUMN user_id TYPE BIGINT"))
        
        # Re-add foreign key constraint
        await conn.execute(text("ALTER TABLE listings ADD CONSTRAINT listings_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(id)"))
        
        print("Migration completed successfully!")

if __name__ == "__main__":
    asyncio.run(migrate_database())