function [dist, path] = shortest_path_dp(W, s, t)
% W: adjacency matrix of the directed weighted graph
% s: index of the source vertex
% t: index of the target vertex

n = size(W, 1);

% Initialize the distance and predecessor arrays
dist = inf(1, n);
dist(s) = 0;
pred = zeros(1, n);

% Compute the shortest paths
for i = 1:n-1
    for j = 1:n
        for k = 1:n
            if W(j,k) ~= 0 && dist(j) + W(j,k) < dist(k)
                dist(k) = dist(j) + W(j,k);
                pred(k) = j;
            end
        end
    end
end

% Backtrack to find the shortest path
path = [];
curr = t;
while curr ~= s
    path = [curr path];
    curr = pred(curr);
end
path = [s path];

end

