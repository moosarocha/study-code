import copy
class PuzzleState:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.size = len(puzzle)
        self.blank_position = puzzle.index(0)  # หาตำแหน่งของเลข 0 (ช่องว่าง)

    def move(self, direction):
        # สร้างคัดลอก (Copy) ของสถานะปัจจุบันขึ้นมาใหม่เพื่อไม่ให้กระทบของเดิม
        new_state = copy.deepcopy(self)
        
        if direction == 'up' and new_state.blank_position >= 3:
            #น้อยกว่า 3 จะลงไม่ได้
            # สลับตำแหน่งกับตัวเลขที่อยู่ด้านบน
            target_idx = new_state.blank_position - 3
            new_state.puzzle[new_state.blank_position], new_state.puzzle[target_idx] = \
                new_state.puzzle[target_idx], new_state.puzzle[new_state.blank_position]
            new_state.blank_position = target_idx
            
        elif direction == 'down' and new_state.blank_position < 6:
            #น้อยกว่า 6 ลงไม่ได้
            # สลับตำแหน่งกับตัวเลขที่อยู่ด้านล่าง
            target_idx = new_state.blank_position + 3
            new_state.puzzle[new_state.blank_position], new_state.puzzle[target_idx] = \
                new_state.puzzle[target_idx], new_state.puzzle[new_state.blank_position]
            new_state.blank_position = target_idx
            
        elif direction == 'left' and new_state.blank_position % 3 != 0:
            # หารด้วย 3 ลงตัวจะชิดซ้าย
            # สลับตำแหน่งกับตัวเลขที่อยู่ด้านซ้าย
            target_idx = new_state.blank_position - 1
            new_state.puzzle[new_state.blank_position], new_state.puzzle[target_idx] = \
                new_state.puzzle[target_idx], new_state.puzzle[new_state.blank_position]
            new_state.blank_position = target_idx
            
        elif direction == 'right' and (new_state.blank_position + 1) % 3 != 0:
            # +1 หารด้วย 3
            # สลับตำแหน่งกับตัวเลขที่อยู่ด้านขวา
            target_idx = new_state.blank_position + 1
            new_state.puzzle[new_state.blank_position], new_state.puzzle[target_idx] = \
                new_state.puzzle[target_idx], new_state.puzzle[new_state.blank_position]
            new_state.blank_position = target_idx
            
        else:
            return None  # ถ้าเดินไปทิศนั้นไม่ได้ให้ส่งค่า None กลับไป
            
        return new_state


# =====================================================================
# 2. ส่วนของฟังก์ชัน Depth-First Search (DFS) สำหรับคำนวณหาคำตอบ
# =====================================================================
def depth_first_search(initial_state, goal_state):
    # ใช้ Stack เก็บ Tuple ของ (สถานะปัจจุบัน, เส้นทางการเดินทิศทางที่ผ่านมา)
    stack = [(initial_state, [])]
    visited = set()  # เก็บสถานะที่เคยไปสำรวจมาแล้วเพื่อป้องกันการเกิด Loop ซ้ำ

    while stack:
        current_state, path = stack.pop()

        # ตรวจสอบว่าสถานะปัจจุบันตรงกับสถานะเป้าหมาย (Goal) หรือยัง
        if current_state.puzzle == goal_state.puzzle:
            return path

        # บันทึกสถานะปัจจุบันลงในกลุ่มที่เคยไปแล้ว
        visited.add(tuple(current_state.puzzle))

        # วนลูปเพื่อทดลองขยับไปในทั้ง 4 ทิศทาง
        for direction in ['up', 'down', 'left', 'right']:
            new_state = current_state.move(direction)
            #ส่วนของตรงนี้คือ จะเริ่มจาก light ก่อน แล้ว ลงไปทาง left และเรื่อยๆ คล้ายการคิดแบบกินเลย์

            # ตรวจสอบว่าขยับได้จริง และผลลัพธ์นั้นยังไม่เคยถูกเข้าไปสำรวจ
            if new_state is not None and tuple(new_state.puzzle) not in visited:
                stack.append((new_state, path + [direction]))

    return None  # หากหาคำตอบไม่ได้เลยจะส่งกลับเป็น None


#example
if __name__ == "__main__":
    # กำหนดกระดานเริ่มต้น (เลข 0 คือช่องว่าง)
    initial_puzzle = [1, 2, 3, 4, 0, 5, 6, 7, 8]
    # กำหนดกระดานเป้าหมายที่ต้องการ
    goal_puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    # สร้าง Instance ของ PuzzleState
    initial_state = PuzzleState(initial_puzzle)
    goal_state = PuzzleState(goal_puzzle)

    print("กำลังคำนวณหาเส้นทางคำตอบด้วย DFS... (อาจใช้เวลาสักครู่)")
    solution_path = depth_first_search(initial_state, goal_state)

    if solution_path is not None:
        print("Solution Path:", solution_path)
    else:
        print("No solution found.")