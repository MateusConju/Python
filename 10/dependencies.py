class PageQuery:
    def __init__(self, page:int = 1, size:int = 10):
        self.page = page
        self.size = size
        self.offset = (page-1) + size

class RoleChecker:
    def __init__(self, required_role:str):
        self.required_role = required_role

    def __cal__(self, user_role:str = 'guest'):
        if user_role != self.required_role:
            raise HTTPException(403, detail=f"Requer Papel: {self.required_role}")
        return True