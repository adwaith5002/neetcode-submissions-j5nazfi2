class TrieNode:
    def __init__(self):
        self.children={}
        self.endofWord=False
    
    def addWord(self,word):
        curr=self
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.endofWord=True
        return
class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        
        for word in words:
            root.addWord(word)
        visited=set()
        res=set()

        def dfs(root,r,c,wordsoFar):
            if ((r,c) in visited or r<0 or c<0 or r>len(board)-1 or c>len(board[0])-1 or board[r][c] not in root.children):
                return
            visited.add((r,c))
            root=root.children[board[r][c]]
            wordsoFar+=board[r][c]
            if root.endofWord:
                res.add(wordsoFar)
            dfs(root,r-1,c,wordsoFar)
            dfs(root,r+1,c,wordsoFar)
            dfs(root,r,c+1,wordsoFar)
            dfs(root,r,c-1,wordsoFar)
            visited.remove((r,c))


        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(root,i,j,"")
        return list(res)

