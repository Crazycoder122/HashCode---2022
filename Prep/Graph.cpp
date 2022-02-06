#include<bits/stdc++.h>


using namespace std;




class Graph{
    public:
    int numNodes;
    vector<vector<int>>adj_list;


    Graph(vector<vector<int>>a)
    {
        vector<int>temp;
        for(int i = 0;i<a.size();i++)
        {
            temp.clear();
            for(int j = 0;j<a[0].size();j++)
            {
                temp.push_back(a[i][j]);
            }

            adj_list.push_back(temp);
        }

        numNodes = a.size();
    }


    void DFS(int start){
        vector<int>visited;
        stack<int> nodes;

        nodes.push(start);

        // While the stack is not empty, do the following
        while(!nodes.empty()){

            // Getting the Node to be Explored and popping it from the stack
            int present = nodes.top();
            nodes.pop();

            // Seeing if the node has already been traversed
            if(find(visited.begin(),visited.end(),present) != visited.end())
            {
                continue;
            }

            // Adding the present Node to the list of Visited Nodes
            visited.push_back(present);

            // Printing the Node
            cout<<present<<" ";

            // Getting all its neighbours
            for(int i = 0;i<numNodes;i++)
            {
                if(adj_list[present - 1][i] == 1)
                    nodes.push(i);
            }
        }
    }


    
};


int main(){
    vector<vector<int>>adj_list = {{0,1,0,0,1},{1,0,1,1,1},{0,1,0,1,0},{0,1,1,0,1},{1,1,0,1,0}};


    Graph *g1 = new Graph(adj_list);
    g1 -> DFS(3);

    return 0;
}